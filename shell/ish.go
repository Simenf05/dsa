package main

import (
	"bufio"
	"errors"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
	"syscall"
)

var PATH = ".:"

func cwd() string {
    buf := make([]byte, syscall.PathMax)
    _, err := syscall.Getcwd(buf)
    if err != nil {
        panic(err)
    }
    text := string(buf)
    return text
}

func exit(args []string) {
    status := 0
    if len(args) <= 1 {
        syscall.Exit(status)
    }

    status, err := strconv.Atoi(args[1])
    if err != nil {
        syscall.Exit(1)
    }
    syscall.Exit(status)
}

func echo(fd int, args []string) {
    string := strings.Join(args[1:], " ")
    string += "\n"

    _, err := syscall.Write(fd, []byte(string))
    if err != nil {
        panic(err)
    }
}

func cd(args []string) error {

    if len(args) < 2 {
        panic("cd needs two args")
    }

    path := args[1]
    err := syscall.Chdir(path);
    return err 
}

func parseLine(reader bufio.Reader) ([]string, error) {

    fmt.Printf("%s > ", cwd())
    text, err := reader.ReadString('\n')

    if err == io.EOF {
        fmt.Println()
        syscall.Exit(0)
    }

    if err != nil {
        return nil, err
    }

    text = text[:len(text)-1]

    seperateOnQuote := strings.Split(text, "\"")

    if len(seperateOnQuote) % 2 == 0 {
        return nil, errors.New("Not matching amounts of quotes.")
    }

    args := make([]string, 0)

    for i, segment := range seperateOnQuote {

        if i % 2 != 0 {
            args = append(args, segment)
            continue
        }

        spaceSplit := strings.Split(segment, " ")

        for _, text := range spaceSplit {
            if len(text) == 0 {
                continue
            }

            args = append(args, text)
        }

    }

    return args, nil
}

func parseArgs(args []string) {
    if args[0] == "" {
        return
    }

    switch args[0] {
    case "cd":
        cd(args)
    case "echo":
        echo(int(os.Stdout.Fd()), args)
    case "exit":
        exit(args)
    default:
        forkProcess(os.Stdin.Fd(), os.Stdout.Fd(), os.Stderr.Fd(), args)
    }
}


func forkProcess(in uintptr, out uintptr, err uintptr, args []string) {

    attr := new(syscall.ProcAttr)
    attr.Files = []uintptr{in, out, err}
    attr.Env = []string{PATH}

    pathArr := strings.Split(PATH, ":")

    for _, dir := range pathArr {

        execPath := dir + "/" + args[0]
        err := syscall.Access(execPath, syscall.F_OK)

        if err != nil {
            continue
        }

        args[0] = execPath
        pid, err := syscall.ForkExec(execPath, args, attr)

        if err != nil {
            panic(err)
        }

        var status syscall.WaitStatus
        _, err = syscall.Wait4(pid, &status, 0, nil)

        if err != nil {
            panic(err)
        }
        return
    }

    fmt.Printf("'%s' not found\n", args[0])
}

func main() {
    reader := bufio.NewReader(os.Stdin)

    envPath, found := syscall.Getenv("PATH")

    if found {
        PATH += envPath
    }

    for {
        args, err := parseLine(*reader)

        if err != nil {
            fmt.Println(err)
            continue
        }

        parseArgs(args)
    }
}
